angular.module('ProspectPassApp')
    .controller('ProspectUserCtrl', function ProspectUserCtrl() {
        this.passes = [
            {
                'name': 'Olivia Johnston',
                'netid': 'oliviaj',
                'memberName': 'Yijia Liang',
                'club': 'Princeton Tower Club',
                'date': '05/13/18',
                'color': '#050505',
                'transferable': true
            },
            {
                'name': 'Olivia Johnston',
                'netid': 'oliviaj',
                'memberName': 'Sam Arnesen',
                'club': 'The Tiger Inn',
                'date': '05/13/18',
                'color': '#505050',
                'transferable': false
            }
        ];

        this.name = "Olivia Johnston";
});
