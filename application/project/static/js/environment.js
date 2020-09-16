socket.on('{{environment}}', function(msg) {
    console.log('here working...')
    console.log('{{environment}} working...' + msg);
});