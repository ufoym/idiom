function FetchCtrl($scope, $http, $timeout) {

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
            $scope.count = response.data.responseData.cursor.estimatedResultCount;
            $scope.examples = response.data.responseData.results;
        });
    };
}