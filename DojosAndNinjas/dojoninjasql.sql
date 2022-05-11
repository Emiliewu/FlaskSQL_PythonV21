-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema books_flask_schema
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema books_flask_schema
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `books_flask_schema` DEFAULT CHARACTER SET utf8 ;
-- -----------------------------------------------------
-- Schema dn_mn_flask_schema
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema dn_mn_flask_schema
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `dn_mn_flask_schema` DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci ;
USE `books_flask_schema` ;

-- -----------------------------------------------------
-- Table `books_flask_schema`.`books`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `books_flask_schema`.`books` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(45) NULL,
  `num_of_pages` VARCHAR(45) NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL DEFAULT NOW(),
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `books_flask_schema`.`authors`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `books_flask_schema`.`authors` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL DEFAULT NOW(),
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `books_flask_schema`.`favorites`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `books_flask_schema`.`favorites` (
  `authors_id` INT NOT NULL,
  `books_id` INT NOT NULL,
  INDEX `fk_favorites_authors_idx` (`authors_id` ASC),
  INDEX `fk_favorites_books1_idx` (`books_id` ASC),
  CONSTRAINT `fk_favorites_authors`
    FOREIGN KEY (`authors_id`)
    REFERENCES `books_flask_schema`.`authors` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_favorites_books1`
    FOREIGN KEY (`books_id`)
    REFERENCES `books_flask_schema`.`books` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

USE `dn_mn_flask_schema` ;

-- -----------------------------------------------------
-- Table `dn_mn_flask_schema`.`courses`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dn_mn_flask_schema`.`courses` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL DEFAULT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 5
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_unicode_ci;


-- -----------------------------------------------------
-- Table `dn_mn_flask_schema`.`dojos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dn_mn_flask_schema`.`dojos` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL DEFAULT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 6
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_unicode_ci;


-- -----------------------------------------------------
-- Table `dn_mn_flask_schema`.`ninjas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dn_mn_flask_schema`.`ninjas` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NULL DEFAULT NULL,
  `last_name` VARCHAR(45) NULL DEFAULT NULL,
  `age` INT(11) NULL DEFAULT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT NULL,
  `dojos_id` INT(11) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_ninjas_dojos_idx` (`dojos_id` ASC),
  CONSTRAINT `fk_ninjas_dojos`
    FOREIGN KEY (`dojos_id`)
    REFERENCES `dn_mn_flask_schema`.`dojos` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 6
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_unicode_ci;


-- -----------------------------------------------------
-- Table `dn_mn_flask_schema`.`registrations`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dn_mn_flask_schema`.`registrations` (
  `courses_id` INT(11) NOT NULL,
  `ninjas_id` INT(11) NOT NULL,
  INDEX `fk_registrations_courses1_idx` (`courses_id` ASC),
  INDEX `fk_registrations_ninjas1_idx` (`ninjas_id` ASC),
  CONSTRAINT `fk_registrations_courses1`
    FOREIGN KEY (`courses_id`)
    REFERENCES `dn_mn_flask_schema`.`courses` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_registrations_ninjas1`
    FOREIGN KEY (`ninjas_id`)
    REFERENCES `dn_mn_flask_schema`.`ninjas` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 5
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_unicode_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
