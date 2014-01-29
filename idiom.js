function FetchCtrl($scope, $http, $timeout, $sce) {

    // delay call
    var timer = false;
    var delay = 1000;
    $scope.$watch('queryText', function () {
        if (timer) {
            $timeout.cancel(timer)
        }
        timer = $timeout(function () {
            if ($scope.queryText && $scope.queryText.length) {
                $scope.search();
            }
        }, delay)
    });

    // search
    $scope.search = function () {
        var url = "http://ajax.googleapis.com/ajax/services/search/web";
        var params = {
            "v": "1.0",
            "callback": "JSON_CALLBACK",
            "rsz": 8,
            "hl": "en",
            "q": '"' + $scope.queryText + '"'
        }
        $http.jsonp(url, {
            params: params
        }).then(function (response) {
            var count = response.data.responseData.cursor.estimatedResultCount;
            var items = response.data.responseData.results;
            if (count > 0) {
                $scope.idiomaticity = Math.log(count) / Math.LN10 * 10;
            }
            else {
                $scope.idiomaticity = 0;
            }

            $scope.examples = [];
            angular.forEach(items, function(item) {
                $scope.examples.push({
                    content: $sce.trustAsHtml(item.content),
                    title: $sce.trustAsHtml(item.title)
                });
            });
        });
    };
}