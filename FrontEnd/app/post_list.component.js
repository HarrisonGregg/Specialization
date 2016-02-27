System.register(['angular2/core', './post'], function(exports_1, context_1) {
    "use strict";
    var __moduleName = context_1 && context_1.id;
    var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
        var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
        if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
        else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
        return c > 3 && r && Object.defineProperty(target, key, r), r;
    };
    var __metadata = (this && this.__metadata) || function (k, v) {
        if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
    };
    var core_1, post_1;
    var PostListComponent;
    return {
        setters:[
            function (core_1_1) {
                core_1 = core_1_1;
            },
            function (post_1_1) {
                post_1 = post_1_1;
            }],
        execute: function() {
            PostListComponent = (function () {
                function PostListComponent() {
                    this.postlist = new Array();
                }
                PostListComponent.prototype.addPost = function (newLink) {
                    var post = new post_1.Post(newLink);
                    this.postlist.push(post);
                };
                PostListComponent.prototype.upVote = function (post) {
                    post.upVote();
                };
                PostListComponent.prototype.downVote = function (post) {
                    post.downVote();
                };
                PostListComponent = __decorate([
                    core_1.Component({
                        selector: 'post-list',
                        templateUrl: '/app/templates/post_list.component.html',
                        styleUrls: ['/css/app.component.css']
                    }), 
                    __metadata('design:paramtypes', [])
                ], PostListComponent);
                return PostListComponent;
            }());
            exports_1("PostListComponent", PostListComponent);
        }
    }
});
//# sourceMappingURL=post_list.component.js.map