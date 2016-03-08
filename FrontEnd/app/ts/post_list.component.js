System.register(['angular2/core', './post.service'], function(exports_1, context_1) {
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
    var core_1, post_service_1;
    var PostListComponent;
    return {
        setters:[
            function (core_1_1) {
                core_1 = core_1_1;
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
                PostListComponent.prototype.addPost = function (newLink, newTitle, newTopic) {
                    var _this = this;
                    if (newLink === void 0) { newLink = "http://google.com"; }
                    if (newTitle === void 0) { newTitle = "title"; }
                    if (newTopic === void 0) { newTopic = 1; }
                    this._postService.addPost(newLink, newTitle, newTopic)
                        .subscribe(function (post) { return _this.postlist.push(post); }, function (error) { return _this.errorMessage = error; });
                };
                PostListComponent.prototype.upVote = function (post) {
                    var _this = this;
                    if (post.vote === -1) {
                        post.score++;
                        post.vote = 0;
                    }
                    if (!post.vote) {
                        post.score++;
                        post.vote = 1;
                        this._postService.updateLink(post)
                            .subscribe(function (updatedPost) { return post = updatedPost; }, function (error) { return _this.errorMessage = error; });
                    }
                };
                PostListComponent.prototype.downVote = function (post) {
                    var _this = this;
                    if (post.vote === 1) {
                        post.score--;
                        post.vote = 0;
                    }
                    if (!post.vote) {
                        post.score--;
                        post.vote = -1;
                        this._postService.updateLink(post)
                            .subscribe(function (updatedPost) { return post = updatedPost; }, function (error) { return _this.errorMessage = error; });
                    }
                };
                PostListComponent = __decorate([
                    core_1.Component({
                        selector: 'post-list',
                        templateUrl: 'app/templates/post_list.component.html',
                        styleUrls: ['/app/css/post_list.component.html']
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