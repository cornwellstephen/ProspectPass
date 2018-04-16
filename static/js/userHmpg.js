angular.module('ProspectPassApp')
    .controller('ProspectUserCtrl', function ProspectUserCtrl() {
        this.user = {
            'passes': [
                {
                    'name': 'Olivia Johnston',
                    'netid': 'oliviaj',
                    'memberName': 'Yijia Liang',
                    'club': 'Princeton Tower Club',
                    'date': '05/13/18',
                    'color': '#BAE06B',
                    'transferable': true,
                    'image': 'tower.png'
                },
                {
                    'name': 'Olivia Johnston',
                    'netid': 'oliviaj',
                    'memberName': 'Sam Arnesen',
                    'club': 'The Tiger Inn',
                    'date': '05/13/18',
                    'color': '#BFEBFF',
                    'transferable': false,
                    'image': 'ti.png'
                },
                {
                    'name': 'Olivia Johnston',
                    'netid': 'oliviaj',
                    'memberName': 'Stephen Cornwell',
                    'club': 'University Cottage Club',
                    'date': '05/13/18',
                    'color': '#FFD9D2',
                    'transferable': false,
                    'image': 'cottage.png'
                }
            ],
            'name': "Olivia Johnston"
        };
});
