const express = require("express");
const path = require("path");
const bodyParser = require("body-parser");
const { spawn } = require("child_process");
const { chownSync } = require("fs");
const childPython = spawn('python', ['CustomerFacade.py'] )
// 'AdministratorFacade.py' 
//const childPython = spawn('python',['--version'])
console.log("start the system");

const port = 6845;
const adminController = express();
childPython.
childPython.stdout.on('data', (data) => {
    console.log('stadout' + data)
})
//server static page
adminController.use(express.static(path.join(__dirname, 'index.html')))
adminController.use(express.json());
adminController.use(express.urlencoded({extended: true}));

// go to static page
adminController.get('/', (req, res) => {
    console.log("ddd");
    res.sendFile(path.join(__dirname, 'index.html'));
});

// get all customers
adminController.get('/customers', async(req, res) => {
    
    // update to facade here
    const customers = "";
    res.status(200).json({customers});
});

// add airline
adminController.post('/airline', async(req, res) => {
    try{
        var airline = req.body;
        // facade
        res.status(201).json({
            res: 'success',
            url: 'localhost:8088/airline/' + {airline:0},
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

// add customer
adminController.post('/customers', async(req, res) => {
    try{
        var customer = req.body;
        // facade
        res.status(201).json({
            res: 'success',
            url: 'localhost:8088/customers/' + {customer:0},
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

// add admin
adminController.post('/administrators', async(req, res) => {
    try{
        var admin = req.body;
        // facade
        res.status(201).json({
            res: 'success',
            url: 'localhost:8088/administrators/' + {admin:0},
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

// remove airline
adminController.delete('/airline/:id', async(req, res) => {
    try{
        const airlineId = req.params.id;
        // add facade
        res.status(200).json({
            res: 'success', 
            url: 'localhost:8088/airline/' + {airlineId}
        });
    }
    catch(e){
        res.status(400).send({
            status: 'failed', 
            message: e.message
        })
    }
});

// remove customer
adminController.delete('/customer/:id', async(req, res) => {
    try{
        const customerId = req.params.id;
        // add facade
        res.status(200).json({
            res: 'success', 
            url: 'localhost:8088/customer/' + {customerId}
        });
    }
    catch(e){
        res.status(400).send({
            status: 'failed', 
            message: e.message
        })
    }
});

// remove administrator
adminController.delete('/admin/:id', async(req, res) => {
    try{
        const adminId = req.params.id;
        // add facade
        res.status(200).json({
            res: 'success', 
            url: 'localhost:8088/admin/' + {adminId}
        });
    }
    catch(e){
        res.status(400).send({
            status: 'failed', 
            message: e.message
        })
    }
});

// add country
adminController.post('/country', async(req, res) => {
    try{
        var country = req.body;
        // facade
        res.status(201).json({
            res: 'success',
            url: 'localhost:8088/country/' + {country:0},
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

adminController.listen(port, () => console.log('port' + {port}));
module.exports = adminController;