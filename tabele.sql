
CREATE TABLE address (
  address_id  INT NOT NULL AUTO_INCREMENT,
  address     VARCHAR(100) NULL,
  postal_code VARCHAR(15) NULL,
  city        VARCHAR(20) NULL,
  PRIMARY KEY (address_id)
) ENGINE=InnoDB COMMENT='#3';

CREATE TABLE trip_category (
  category_id   INT NOT NULL AUTO_INCREMENT,
  category_name VARCHAR(25) NULL,
  PRIMARY KEY (category_id)
) ENGINE=InnoDB COMMENT='#1';

CREATE TABLE staff (
  staff_id   INT NOT NULL AUTO_INCREMENT COMMENT 'min 5 pracowników',
  address_id INT NOT NULL,
  first_name VARCHAR(40) NULL,
  last_name  VARCHAR(40) NULL,
  salary     INT NULL COMMENT 'min krajowa, więcej nie płacimy',
  email      VARCHAR(80) NULL,
  hire_date  DATE NULL COMMENT '1.01.2024 min 5 wtedy',
  birth_date DATE NULL COMMENT '18+',
  PRIMARY KEY (staff_id)
) ENGINE=InnoDB COMMENT='#5';

CREATE TABLE customers (
  customer_id  INT NOT NULL AUTO_INCREMENT,
  address_id   INT NOT NULL,
  first_name   VARCHAR(40) NULL,
  last_name    VARCHAR(40) NULL,
  email        VARCHAR(80) NULL,
  phone_number INT NULL,
  birth_date   DATE NULL COMMENT '15+',
  ICE_number   INT NULL,
  PRIMARY KEY (customer_id)
) ENGINE=InnoDB COMMENT='#4';

CREATE TABLE trips (
  trip_id       INT NOT NULL AUTO_INCREMENT COMMENT 'w poprzedni rok zrealizowano min 10 wyjazdów min 5 rodzajów było na nich min 30 osób',
  category_id   INT NOT NULL,
  trip_name     VARCHAR(40) NULL,
  margin        FLOAT NULL COMMENT 'tyle zarabiamy na kliencie',
  begin_date    DATE NULL,
  end_date      DATE NULL,
  abroad        BOOLEAN NULL,
  creation_date DATE NULL COMMENT 'firma musi działać minimum rok zaczynając od 1.01.2024 ale nie musi być od wtedy',
  description   VARCHAR(255) NULL,
  max_spots     INT NULL COMMENT 'max ilość ludzi na wycieczce',
  PRIMARY KEY (trip_id)
) ENGINE=InnoDB COMMENT='#2';

CREATE TABLE costs (
  cost_id INT NOT NULL AUTO_INCREMENT,
  trip_id INT NOT NULL,
  name    VARCHAR(50) NULL,
  amount  FLOAT NULL,
  PRIMARY KEY (cost_id)
) ENGINE=InnoDB COMMENT='#7';

CREATE TABLE payment (
  payment_id   INT NOT NULL AUTO_INCREMENT,
  customer_id  INT NOT NULL,
  staff_id     INT NOT NULL,
  trip_id      INT NOT NULL,
  payment_date TIMESTAMP NULL COMMENT 'musi być po creation_date i przed begin_date (najlepiej jakiś deadline np tydzień przed begin)',
  amount       INT NULL COMMENT 'ilość zakupionych miejsc na wycieczce, nie może przekroczyć liczby miejsc na wycieczce',
  PRIMARY KEY (payment_id)
) ENGINE=InnoDB COMMENT='#6';


-- PAYMENT -> CUSTOMERS
ALTER TABLE payment
  ADD CONSTRAINT FK_customers_TO_payment
    FOREIGN KEY (customer_id)
    REFERENCES customers (customer_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE;

-- PAYMENT -> STAFF
ALTER TABLE payment
  ADD CONSTRAINT FK_staff_TO_payment
    FOREIGN KEY (staff_id)
    REFERENCES staff (staff_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE;

-- PAYMENT -> TRIPS
ALTER TABLE payment
  ADD CONSTRAINT FK_trips_TO_payment
    FOREIGN KEY (trip_id)
    REFERENCES trips (trip_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE;

-- TRIPS -> TRIP_CATEGORY
ALTER TABLE trips
  ADD CONSTRAINT FK_trip_category_TO_trips
    FOREIGN KEY (category_id)
    REFERENCES trip_category (category_id)
    ON DELETE RESTRICT
    ON UPDATE CASCADE;

-- CUSTOMERS -> ADDRESS
ALTER TABLE customers
  ADD CONSTRAINT FK_address_TO_customers
    FOREIGN KEY (address_id)
    REFERENCES address (address_id)
    ON DELETE RESTRICT
    ON UPDATE CASCADE;

-- COSTS -> TRIPS
ALTER TABLE costs
  ADD CONSTRAINT FK_trips_TO_costs
    FOREIGN KEY (trip_id)
    REFERENCES trips (trip_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE;

-- STAFF -> ADDRESS
ALTER TABLE staff
  ADD CONSTRAINT FK_address_TO_staff
    FOREIGN KEY (address_id)
    REFERENCES address (address_id)
    ON DELETE RESTRICT
    ON UPDATE CASCADE;
