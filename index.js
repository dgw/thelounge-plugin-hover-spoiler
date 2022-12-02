"use strict";

module.exports = {
    onServerStart: (api) => {
        api.Stylesheets.addFile("hover-spoiler.css");
    }
}
