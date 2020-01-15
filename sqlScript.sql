SELECT concat(o.OrgName,'|',u.FirstName,'|', u.LastName,'|', rh.ReportName, '|',e.EventCode,'|',e.GMTDateTime,'|',e.EventData) as data
FROM Event e 
        LEFT JOIN ReportHeader rh on e.ContentId = rh.ReportId 
        LEFT JOIN Person u on e.IpSource = u.IpPerson
        LEFT JOIN Organisation o on e.UnitId = o.IpOrg 
        WHERE EventDate = DATE_FORMAT(CURRENT_TIMESTAMP, '%Y-%m-%d')
              AND DATE_FORMAT(GMTDateTime, '%Y%m%d%H%i') >= DATE_FORMAT( DATE_SUB(CURRENT_TIMESTAMP, INTERVAL 2 HOUR), '%Y%m%d%H%i')
              AND EventCode = 'RPTRUN'
              ORDER by GMTDateTime 
              DESC limit 10;
