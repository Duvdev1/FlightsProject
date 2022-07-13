const express = require("express");
const path = require("path");
const bodyParser = require("body-parser");
const spawn = require("child_process").spawn;
const facade = spawn('python', ['./../AnonymousFacade.py'] )

console.log("start the system");

const port = 6845;
const anonymousController = express();

//server static page
anonymousController.use(express.static(path.join(__dirname, 'index.html')))
anonymousController.use(express.json());
anonymousController.use(express.urlencoded({extended: true}));

// go to static page
anonymousController.get('/', (req, res) => {
    console.log("ddd")
    res.sendFile(path.join(__dirname, 'index.html'));
});

// login function
anonymousController.post('/login', async(req, res) => {
    try{
        let username = req.body.username;
        let password = req.body.password;
        // facade
        res.status(201).json({key:5});
    }
    catch(e){
        res.status(400).send({
            status: 'failed',
            message: e.message
        });
    }
});

// add customer
anonymousController.post('/customer', async(req, res) => {
    try{
        var user = req.body.user;
        var customer = req.body.customer;
        // facade
        res.status(201).json({
            res: 'success',
            url: 'localhost:8088/customer/' + {customer:0},
            add
        });
    }
    catch(e){
        res.status(400).send({
            status: 'failed',
            message: e.message
        });
    }

});



anonymousController.listen(port, () => console.log('port' + {port}));
module.exports = anonymousController;