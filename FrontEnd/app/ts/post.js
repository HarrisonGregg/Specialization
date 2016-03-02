System.register([], function(exports_1, context_1) {
    "use strict";
    var __moduleName = context_1 && context_1.id;
    var Post;
    return {
        setters:[],
        execute: function() {
            Post = (function () {
                function Post(newLink, newTitle, newTopic) {
                    this.url = newLink;
                    this.topic = newTitle;
                    this.title = newTopic;
                }
                return Post;
            }());
            exports_1("Post", Post);
        }
    }
});
//# sourceMappingURL=post.js.map