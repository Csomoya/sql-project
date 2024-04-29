CREATE SCHEMA sql_project;

SHOW SCHEMAS;

CREATE TABLE ProductTree (
category varchar(255),
product_id varchar(255),
product_name varchar(255),
inserted_at timestamp default current_timestamp
);


CREATE TABLE Vulnerabilities (
title varchar(255),
cve varchar(255),
description varchar(255),
threats varchar(255),
fixed_build varchar(255),
inserted_at timestamp default current_timestamp
);
/*
CREATE TABLE CVE(
CVE varchar(255),
Description varchar(255),
Vendor varchar(255),
Product varchar(255),
Ransomware varchar(255),
Due_Date date,
Action varchar(255),
inserted_at timestamp default current_timestamp
);

DELETE FROM CVE
WHERE inserted_at = '2024-04-29 02:34:00'
*/