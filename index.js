// Get all the reports for the reports.html table
//const logger = require("./logger");
//logger.info('start with ajax, import all reports for the html');
$(document).ready(function() {
    $.ajax({url:"/reports"}).then(
        // after success
        function(reports){
            //logger.info(reports);
            const reports_ls = reports.reports;
            const reports_table = $('#reports');
            reports_table.find("tr:gt(0)").remove();
            $.each (reports_ls, (i, report) => {
                reports_table.append(
                    '<tr><td class="fw-lighter">${report.id}</td><td class="fw-lighter">${report.licene_id}</td><td class="fw-lighter">${report.drive_id}</td><td class="fw-lighter">${report.speed}</td>');
            })
        }
        // after failed
        ,function(err){
           // logger.error(error);
           console.error(err);
        }
    );
});