var alreadyImageMapped = {};
        var tabContent = {};
function replaceRibbonContent(tabName) {
          $('#ribbon').empty();
          $('#ribbon').append(tabContent[tabName]);
          if (alreadyImageMapped[tabName]) {
            return;
          }
          alreadyImageMapped[tabName] = true;
          $('img').mapster({
		render_highlight: {
			fillOpacity: 0.4,
			fillColor: "FFFFFF",

          },
		fillOpacity: 0.1,
           fillColor: "000000",
    	  });
        }



	$(document).ready(function() {

        var ribbon = $('#ribbon');

        for (var tabName in tabs) {
          specificTabContent = $('<div>');
          specificTabContent.load(tabName + '.html');
          tabContent[tabName] = specificTabContent;
        }

		$('img').mapster({
		render_highlight: {
			fillOpacity: 0.4,
			fillColor: "FFFFFF",

        },
		fillOpacity: 0.1,
        fillColor: "000000",
    	});

    	ribbon.on('click', '#home', function() {
			replaceRibbonContent('home');
		});

    	ribbon.on('click', '#layout', function() {
			replaceRibbonContent('layout');
		});

		ribbon.on('click', '#document-elements', function() {
			replaceRibbonContent('document-elements');
		});

		ribbon.on('click', '#tables', function() {
			replaceRibbonContent('tables');
		});

    	ribbon.on('click', '#charts', function() {
		  replaceRibbonContent('charts');
		});

    ribbon.on('click', '#smartart', function() {
		  replaceRibbonContent('smartart');
		});

    	ribbon.on('click', '#review', function() {
		  replaceRibbonContent('review');
		});

           replaceRibbonContent(currentTab);
	});
