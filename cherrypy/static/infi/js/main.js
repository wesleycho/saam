(function($) {
    var handler = null,
            page = 1,
            isLoading = false,
            apiURL = 'http://localhost:8080/api/collections';

    // Prepare layout options.
    var options = {
        autoResize: true, // This will auto-update the layout when the browser window is resized.
        container: $('#tiles'), // Optional, used for some extra CSS styling
        offset: 2, // Optional, the distance between grid items
        itemWidth: 210 // Optional, the width of a grid item
    };
    var rows = 30;
    var start = 0;
    var url;
    var currentId;
    var allData = [];

    /**
     * When scrolled all the way to the bottom, add more tiles.
     */
    function onScroll(event) {
        // Only check when we're not still waiting for data.
        if (!isLoading) {
            // Check if we're within 100 pixels of the bottom edge of the broser window.
            var closeToBottom = ($(window).scrollTop() + $(window).height() > $(document).height() - 100);
            if (closeToBottom) {
                loadData();
            }
        }
    }
    ;

    /**
     * Refreshes the layout.
     */
    function applyLayout() {
        options.container.imagesLoaded(function() {
            // Create a new layout handler when images have loaded.
            handler = $('#tiles li');
            handler.wookmark(options);
        });
    }
    ;

    /**
     * Loads data from the API.
     */
    function loadData() {
        isLoading = true;
        $('#loaderCircle').show();
        start += rows;
        $.ajax({
            url: apiURL,
            dataType: 'json',
            data: {
                q: "rome",
                rows: rows,
                start: start,
            }, // Page parameter to make sure we load new data
            success: onLoadData,
            error: function(e) {
                console.log("Error: could not load data from API");
            }
        });
    }
    ;

    /**
     * Receives data from the API, creates HTML for images and updates the layout
     */
    function onLoadData(data) {
        isLoading = false;
        $('#loaderCircle').hide();

        // Increment page index for future calls.
        page++;

        // Create HTML for the images.
        var html = '';
        var i = 0, length = data.length, image;

        var docs = data.response.docs;
        for (var i = 0; i < docs.length; i++) {
            var descriptiveNonRepeating = docs[i].descriptiveNonRepeating;
            var image = descriptiveNonRepeating.online_media.media[0].content;
            var thumbnail = descriptiveNonRepeating.online_media.media[0].thumbnail;
            var title = descriptiveNonRepeating.title.content;
            var id = i + start;
            html += '<li>';

            // Image tag (preview in Wookmark are 200px wide, so we calculate the height based on that).
            html += '<a class="ajax-popup img-pop" href="image.html" data-id="' + id + '">';
            html += '<img data-id="' + id + '" src="' + image + '" width="200" height="200"/></a>';

            // Image title.
            html += '<p>' + title + '</p>';

            html += '</li>';
        }
        allData.push(docs);

        // Add image HTML to the page.
        $('#tiles').append(html);

        $('.img-pop').click(function(e) {
            var srcElement = e.srcElement;
            var dataArray = allData[0];
            var id = parseInt(srcElement.dataset.id) - start;
            var item = dataArray[id];

            url = srcElement.src;
            currentId = id;
            console.log(item);
            e.preventDefault();
        });

        $('.ajax-popup').magnificPopup({
            type: 'ajax',
            closeBtnInside: false,
            callbacks: {
                open: function(e) {
                },
                ajaxContentAdded: function(e) {
                    // dynamically load image
                    var img = document.createElement("img");
                    var item = allData[0][currentId];
                    img.onload = function(e) {
                        var container = document.getElementById("imageContainer");
                        container.appendChild(e.target);
                    }
                    var descriptiveNonRepeating = item.descriptiveNonRepeating;
                    var image = descriptiveNonRepeating.online_media.media[0].content;
                    var thumbnail = descriptiveNonRepeating.online_media.media[0].thumbNail;
                    var title = descriptiveNonRepeating.title.content;
                    var freetext = item.freetext;
                    var date = freetext.date[0].content;
                    var description = freetext.physicalDescription[0].content;

                    $('#title').text(title);
                    $('#date').text(date);
                    $('#description').text(description);

                    img.setAttribute("src", url);
                }
            }
        });

        // Apply layout.
        applyLayout();
    }
    ;

    // Capture scroll event.
    $(document).bind('scroll', onScroll);

    // Load first data from the API.
    loadData();
})(jQuery);