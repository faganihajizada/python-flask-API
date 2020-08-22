USE students;
CREATE TABLE `students` (
  `student_id` bigint(20) NOT NULL AUTO_INCREMENT,
  `student_name` varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL,
  `student_email` varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL,
  `university` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`student_id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;