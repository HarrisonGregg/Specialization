System.register(['angular2/core', 'angular2/http', './post', 'rxjs/Observable'], function(exports_1, context_1) {
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
    var core_1, http_1, post_1, Observable_1, http_2;
    var PostService;
    return {
        setters:[
            function (core_1_1) {
                core_1 = core_1_1;
            },
            function (http_1_1) {
                http_1 = http_1_1;
                http_2 = http_1_1;
            },
            function (post_1_1) {
                post_1 = post_1_1;
            },
            function (Observable_1_1) {
                Observable_1 = Observable_1_1;
            }],
        execute: function() {
            PostService = (function () {
                function PostService(http) {
                    this.http = http;
                    this._postlistUrl = 'http://education-project.herokuapp.com/topicLinks/Bananas/'; // URL to web api
                    this._addlinkUrl = 'http://education-project.herokuapp.com/links/';
                    this._updatelinkUrl = 'http://education-project.herokuapp.com/links/';
                }
                PostService.prototype.getPostList = function () {
                    console.log("services get called");
                    return this.http.get(this._postlistUrl)
                        .map(function (res) { return res.json(); })
                        .do(function (data) { return console.log(data); })
                        .catch(this.handleError);
                };
                PostService.prototype.addPost = function (newLink, newTitle, newTopic) {
                    if (newTitle === void 0) { newTitle = ""; }
                    if (newTopic === void 0) { newTopic = 1; }
                    var newPost = new post_1.Post(newLink, newTopic, newTitle);
                    console.log(newPost);
                    var body = JSON.stringify(newPost);
                    var headers = new http_2.Headers({ 'Content-Type': 'application/json' });
                    var options = new http_2.RequestOptions({ headers: headers });
                    return this.http.post(this._addlinkUrl, body, options)
                        .map(function (res) { return res.json(); })
                        .do(function (data) { return console.log("add link", data); })
                        .catch(this.handleError);
                };
                PostService.prototype.updateLink = function (post) {
                    var body = JSON.stringify(post);
                    var headers = new http_2.Headers({ 'Content-Type': 'application/json' });
                    var options = new http_2.RequestOptions({ headers: headers,
                        url: this._updatelinkUrl + post.pk + "/" });
                    return this.http.put(this._updatelinkUrl, body, options)
                        .map(function (res) { return res.json(); })
                        .do(function (data) { return console.log("update link", data); })
                        .catch(this.handleError);
                };
                PostService.prototype.handleError = function (error) {
                    // in a real world app, we may send the error to some remote logging infrastructure
                    // instead of just logging it to the console
                    console.error(error);
                    return Observable_1.Observable.throw(error.json().error || 'Server error');
                };
                PostService = __decorate([
                    core_1.Injectable(), 
                    __metadata('design:paramtypes', [http_1.Http])
                ], PostService);
                return PostService;
            }());
            exports_1("PostService", PostService);
        }
    }
});
//# sourceMappingURL=post.service.js.map