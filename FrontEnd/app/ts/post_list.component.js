System.register(['angular2/core', './post', './post.service'], function(exports_1, context_1) {
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
    var core_1, post_1, post_service_1;
    var PostListComponent;
    return {
        setters:[
            function (core_1_1) {
                core_1 = core_1_1;
            },
            function (post_1_1) {
                post_1 = post_1_1;
            },
            function (post_service_1_1) {
                post_service_1 = post_service_1_1;
            }],
        execute: function() {
            PostListComponent = (function () {
                function PostListComponent(_postService) {
                    this._postService = _postService;
                    this.postlist = new Array();
                }
                PostListComponent.prototype.ngOnInit = function () { this.getPostList(); };
                PostListComponent.prototype.getPostList = function () {
                    var _this = this;
                    console.log('component getpostlist called');
                    this._postService.getPostList()
                        .subscribe(function (postlist) { return _this.postlist = postlist; }, function (error) { return _this.errorMessage = error; });
                };
                PostListComponent.prototype.addPost = function (newLink) {
                    var post = new post_1.Post(newLink);
                    this.postlist.push(post);
                    console.log(post.link);
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
                        template: "\n\t\t<input #newLink\n      \t\t(keyup.enter)=\"addPost(newLink.value)\"\n      \t\t(blur)=\"newLink.value='' \">\n\n    \t<button (click)=addPost(newLink.value)>PostLink</button>\n    \t<ul>\n    \t\t<li *ngFor=\"#post of postlist\">{{post.link}}\n    \t\t\t<button (click)=upVote(post)>upvote</button>\n    \t\t\t<button (click)=downVote(post)>downvote</button>\n    \t\t\t<div>vote = {{ post.vote }}</div>\n    \t\t</li>\n    \t</ul>\n\t"
                    }), 
                    __metadata('design:paramtypes', [post_service_1.PostService])
                ], PostListComponent);
                return PostListComponent;
            }());
            exports_1("PostListComponent", PostListComponent);
        }
    }
});
//# sourceMappingURL=post_list.component.js.map