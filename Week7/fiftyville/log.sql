-- Keep a log of any SQL queries you execute as you solve the mystery.

SELECT * FROM crime_scene_reports WHERE year = 2023 AND month = 7 AND day = 28 AND street = "Humphrey Street";

SELECT * FROM interviews WHERE year = 2023 AND month = 7 AND day = 28;

SELECT * FROM bakery_security_logs WHERE year = 2023 AND month = 7 AND day = 28 AND activity = "exit" AND hour = 10 AND minute BETWEEN 15 AND 25;

SELECT * FROM atm_transactions WHERE year = 2023 AND month = 7 AND day = 28 AND transaction_type = "withdraw" AND atm_location = "Leggett Street";

SELECT id FROM airports WHERE city = "Fiftyville";

SELECT * FROM flights WHERE year = 2023 AND month = 7 AND day = 29 AND origin_airport_id = 8 ORDER BY hour , minute LMIT 1;

SELECT * FROM bank_accounts WHERE account_number IN (SELECT account_number FROM atm_transactions WHERE year = 2023 AND month = 7 AND day = 28 AND transaction_type = "withdraw" AND atm_location = "Leggett Street");

SELECT * FROM people WHERE id IN (SELECT person_id FROM bank_accounts WHERE account_number IN (SELECT account_number FROM atm_transactions WHERE year = 2023 AND month = 7 AND day = 28 AND transaction_type = "withdraw" AND atm_location = "Leggett Street"));

SELECT * FROM bakery_security_logs AS b, people AS p WHERE b.license_plate = p.license_plate AND b.license_plate IN (SELECT license_plate FROM bakery_security_logs WHERE year = 2023 AND month = 7 AND day = 28 AND activity = "exit" AND hour = 10 AND minute BETWEEN 15 AND 25) AND p.license_plate IN (SELECT license_plate FROM people WHERE id IN (SELECT person_id FROM bank_accounts WHERE account_number IN (SELECT account_number FROM atm_transactions WHERE year = 2023 AND month = 7 AND day = 28 AND transaction_type = "withdraw" AND atm_location = "Leggett Street")));

SELECT * FROM phone_calls WHERE year = 2023 AND month = 7 AND day = 28 AND duration > 60;

SELECT * FROM people WHERE phone_number IN (SELECT caller FROM phone_calls WHERE year = 2023 AND month = 7 AND day = 28 AND duration < 60);

SELECT * FROM passengers WHERE flight_id = 36;

SELECT * FROM people WHERE name IN ("Diana", "Bruce") AND passport_number IN (SELECT passport_number FROM passengers WHERE flight_id = 36);

SELECT * FROM people WHERE phone_number = (SELECT receiver FROM phone_calls WHERE year = 2023 AND month = 7 AND day = 28 AND duration < 60 AND caller = (SELECT phone_number FROM people WHERE name IN ("Diana", "Bruce") AND passport_number IN (SELECT passport_number FROM passengers WHERE flight_id = 36)));

SELECT city FROM airports WHERE id = 4;

