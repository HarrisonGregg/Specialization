System.register([], function(exports_1, context_1) {
    "use strict";
    var __moduleName = context_1 && context_1.id;
    var Post;
    return {
        setters:[],
        execute: function() {
            Post = (function () {
                function Post(newLink) {
                    this.link = newLink;
                    this.vote = 0;
                }
                Post.prototype.upVote = function () {
                    this.vote++;
                };
                Post.prototype.downVote = function () {
                    if (this.vote) {
                        this.vote--;
                    }
                };
                return Post;
            }());
            exports_1("Post", Post);
        }
    }
});
//# sourceMappingURL=post.js.map