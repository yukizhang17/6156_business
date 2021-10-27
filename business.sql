use business;

CREATE TABLE `business` (
  `bid` varchar(128) NOT NULL,
  `business_name` varchar(45) DEFAULT NULL,
  `phone_number` varchar(45) DEFAULT NULL,
  `email` varchar(128) NOT NULL,
  PRIMARY KEY (`bid`),
  UNIQUE KEY `email_UNIQUE` (`email`)
);

CREATE TABLE `product` (
  `pid` varchar(128) NOT NULL,
  `product_name` varchar(128) DEFAULT NULL,
  `price` varchar(45) DEFAULT NULL,
  `description` TEXT DEFAULT NULL,
  `bid` varchar(128) NOT NULL,
   PRIMARY KEY (`pid`),
  CONSTRAINT `bid_from_product_to_business` FOREIGN KEY (`bid`) REFERENCES `business` (`bid`)
);

CREATE TABLE `address` (
  `baid` varchar(128) NOT NULL,
  `street_name1` varchar(255) DEFAULT NULL,
  `street_name2` varchar(255) DEFAULT NULL,
  `city` varchar(128) DEFAULT NULL,
  `state` varchar(45) DEFAULT NULL,
  `zipcode` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`baid`)
);

CREATE TABLE `business_address` (
  `bid` varchar(128) NOT NULL,
  `baid` varchar(128) NOT NULL,
  PRIMARY KEY (`bid`,`baid`),
  KEY `baid_idx` (`baid`),
  CONSTRAINT `baid_from_business_address_to_address` FOREIGN KEY (`baid`) REFERENCES `address` (`baid`),
  CONSTRAINT `bid_from_business_address_to_business` FOREIGN KEY (`bid`) REFERENCES `business` (`bid`)
);

CREATE TABLE `business_productaddressaddressbaid` (
  `bid` varchar(128) NOT NULL,
  `pid` varchar(128) NOT NULL,
  PRIMARY KEY (`bid`,`pid`),
  KEY `pid_idx` (`pid`),
  CONSTRAINT `pid_from_business_product_to_product` FOREIGN KEY (`pid`) REFERENCES `product` (`pid`),
  CONSTRAINT `bid_from_business_product_to_business` FOREIGN KEY (`bid`) REFERENCES `business` (`bid`)
);


