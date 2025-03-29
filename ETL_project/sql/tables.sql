-- Drop tables if they exist (for clean setup)
DROP TABLE IF EXISTS fact_web_access;
DROP TABLE IF EXISTS dim_time;
DROP TABLE IF EXISTS dim_client;
DROP TABLE IF EXISTS dim_file;
DROP TABLE IF EXISTS dim_geolocation;
DROP TABLE IF EXISTS dim_referrer;

-- dim_time
CREATE TABLE dim_time (
    timeid SERIAL PRIMARY KEY,
    fulldate DATE,
    day INTEGER,
    month INTEGER,
    quarter INTEGER,
    year INTEGER
);

-- dim_client
CREATE TABLE dim_client (
    clientid SERIAL PRIMARY KEY,
    os VARCHAR(100),
    browser VARCHAR(100),
    ipaddress VARCHAR(50),
    host VARCHAR(100),
    iscrawler BOOLEAN
);

-- dim_file
CREATE TABLE dim_file (
    fileid SERIAL PRIMARY KEY,
    filetype VARCHAR(50),
    extension VARCHAR(50),
    size INTEGER
);

-- dim_geolocation
CREATE TABLE dim_geolocation (
    geoid SERIAL PRIMARY KEY,
    city VARCHAR(100),
    state VARCHAR(100),
    country VARCHAR(100),
    postcode VARCHAR(20)
);

-- dim_referrer
CREATE TABLE dim_referrer (
    referrerid SERIAL PRIMARY KEY,
    sourceurl TEXT,
    searchengine VARCHAR(50),
    campaign VARCHAR(100)
);

-- fact_web_access
CREATE TABLE fact_web_access (
    factid SERIAL PRIMARY KEY,
    timeid INTEGER REFERENCES dim_time(timeid),
    geoid INTEGER REFERENCES dim_geolocation(geoid),
    clientid INTEGER REFERENCES dim_client(clientid),
    fileid INTEGER REFERENCES dim_file(fileid),
    referrerid INTEGER REFERENCES dim_referrer(referrerid),
    filerequests INTEGER,
    bytesserved INTEGER,
    processingtime INTEGER,
    failures INTEGER,
    visits INTEGER
);
