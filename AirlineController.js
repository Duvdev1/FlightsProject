const express = require("express");
const path = require("path");
const bodyParser = require("body-parser");
const spawn = require("child_process").spawn;
const facade = spawn('python', ['./../CustomerFacade.py'] )

console.log("start the system");

const port = 6845;
const airlineController = express();

//server static page
airlineController.use(express.static(path.join(__dirname, 'index.html')))
airlineController.use(express.json());
airlineController.use(express.urlencoded({extended: true}));

// go to static page
airlineController.get('/', (req, res) => {
    console.log("ddd")
    res.sendFile(path.join(__dirname, 'index.html'));
});

// add flight
airlineController.post('/flight', async(req, res) => {
    try{
        var flight = req.body;
        // facade
        res.status(201).json({
            res: 'success',
            url: 'localhost:8088/flight/' + {flight:0},
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

// remove flight
airlineController.delete('/flight/:id', async(req, res) => {
    try{
        const flight_id = req.params.id;
        // add facade
        res.status(200).json({
            res: 'success', 
            url: 'localhost:8088/ticket/' + {flight_id}
        });
    }
    catch(e){
        res.status(400).send({
            status: 'failed', 
            message: e.message
        })
    }
});

// get flights by airline
airlineController.get('/airline/:id', async(req, res) => {
    const airlineId = req.params.id;
    // update to facade here
    const customer = "";
    res.status(200).json({customer});
});

// update airline
airlineController.post('/airline/:id', async(req, res) => {
    try{
        var airline = req.body;
        // facade
        res.status(201).json({
            res: 'success',
            url: 'localhost:8088/airline/' + {airline:0},
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

// update flight
airlineController.post('/flight/:id', async(req, res) => {
    try{
        var flight = req.body;
        // facade
        res.status(201).json({
            res: 'success',
            url: 'localhost:8088/flight/' + {flight:0},
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



airlineController.listen(port, () => console.log('port' + {port}));
module.exports = airlineController;