function htmz(frame) {
    setTimeout(() => {
        // Error handling
        // hacky way to get the frame's current status code
        const status =
          frame.contentWindow.performance.getEntriesByType("navigation")[0]
            ?.responseStatus;

        if (status && (status < 200 || status > 299)) {
          alert(frame.contentWindow.document.title);
          return;
        }

        // replace item in main body with id matching the query fragment
        document
            .querySelector(frame.contentWindow.location.hash || null)
            ?.replaceWith(...frame.contentDocument.body.childNodes)
    });
}
