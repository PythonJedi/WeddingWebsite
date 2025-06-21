function htmz(frame) {
    setTimeout(() => {
        // 
        if (frame.className == "") {
            frame.className = "loaded";
            return;
        }

        // Error handling
        // hacky way to get the frame's current status code
        const status =
          frame.contentWindow.performance.getEntriesByType("navigation")[0]
            ?.responseStatus;

        if (status && (status < 200 || status > 299)) {
          alert(frame.contentWindow.document.title);
          return;
        }

        // replace item in main body with id matching the name of the iframe
        document
            .querySelector(frame.name)
            ?.replaceWith(...frame.contentDocument.body.childNodes);
    });
}
