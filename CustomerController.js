const express = require("express");
const path = require("path");
const bodyParser = require("body-parser");
const spawn = require("child_process").spawn;
const facade = spawn('python', ['./../CustomerFacade.py'] )

console.log("start the system");

const port = 6845;
const customerController = express();

//server static page
customerController.use(express.static(path.join(__dirname, 'index.html')))
customerController.use(express.json());
customerController.use(express.urlencoded({extended: true}));

// go to static page
customerController.get('/', (req, res) => {
    console.log("ddd")
    res.sendFile(path.join(__dirname, 'index.html'));
});

// update customer by id
customerController.post('/customer/:id', async(req, res) => {
    try{
        var customer = req.body;
        // facade
        res.status(201).json({
            res: 'success',
            url: 'localhost:8088/customer/' + {customer:0},
            update
        });
    }
    catch(e){
        res.status(400).send({
            status: 'failed',
            message: e.message
        });
    }
});

// add ticket
customerController.post('/ticket', async(req, res) => {
    try{
        var ticket = req.body;
        // facade
        res.status(201).json({
            res: 'success',
            url: 'localhost:8088/ticket/' + {ticket:0},
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

// remove ticket
customerController.delete('/ticket/:id', async(req, res) => {
    try{
        const ticket_id = req.params.id;
        // add facade
        res.status(200).json({
            res: 'success', 
            url: 'localhost:8088/ticket/' + {ticket_id}
        });
    }
    catch(e){
        res.status(400).send({
            status: 'failed', 
            message: e.message
        })
    }
});

// get ticket by customer
customerController.get('/customer/:id', async(req, res) => {
    const customerId = req.params.id;
    // update to facade here
    const customer = "";
    res.status(200).json({customer});
})



customerController.listen(port, () => console.log('port' + {port}));
module.exports = customerController;