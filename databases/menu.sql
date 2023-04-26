CREATE TABLE restaurant(

  id integer PRIMARY KEY,
  name varchar(20),
  description varchar(100),
  rating decimal,
  phone_number varchar(10), 
  hours varchar(100)

);

CREATE TABLE address(

  id integer PRIMARY KEY,
  street_number varchar(10),
  street_name varchar(20),
  city varchar(20),
  state varchar(15),
  google_map_link varchar(50)

);


CREATE TABLE category(
  id char(2) PRIMARY KEY,
  name varchar(20),
  description varchar(200)
);

CREATE TABLE dish(
  id integer PRIMARY KEY,
  name varchar(50),
  description varchar(200), 
  hot_and_spicy boolean
);

CREATE TABLE review(
  id integer PRIMARY KEY,
  rating decimal,
  description varchar(100),
  date date
);

ALTER TABLE restaurant
ADD COLUMN address_id integer REFERENCES address(id) UNIQUE;

ALTER TABLE restaurant
ADD COLUMN reivew_id integer REFERENCES review(id);

CREATE TABLE categories_dishes(

  categories_id char(2) REFERENCES category(id),
  dishes_id integer REFERENCES dish(id),
  price money,
  PRIMARY KEY(categories_id, dishes_id)

);


-- SELECT constraint_name, table_name, column_name
-- FROM information_schema.key_column_usage;

INSERT INTO restaurant VALUES (
  1,
  'Bytes of China',
  'Delectable Chinese Cuisine',
  3.9,
  '6175551212',
  'Mon - Fri 9:00 am to 9:00 pm, Weekends 10:00 am to 11:00 pm'
);

INSERT INTO address VALUES (
  1,
  '2020',
  'Busy Street',
  'Chinatown',
  'MA',
  'http://bit.ly/BytesOfChina'
);

INSERT INTO review VALUES (
  1,
  5.0,
  'Would love to host another birthday party at Bytes of China!',
  '05-22-2020'
);

INSERT INTO review VALUES (
  2,
  4.5,
  'Other than a small mix-up, I would give it a 5.0!',
  '04-01-2020'
);

INSERT INTO review VALUES (
  3,
  3.9,
  'A reasonable place to eat for lunch, if you are in a rush!',
  '03-15-2020'
);

INSERT INTO category VALUES (
  'C',
  'Chicken',
  null
);

INSERT INTO category VALUES (
  'LS',
  'Luncheon Specials',
  'Served with Hot and Sour Soup or Egg Drop Soup and Fried or Steamed Rice  between 11:00 am and 3:00 pm from Monday to Friday.'
);

INSERT INTO category VALUES (
  'HS',
  'House Specials',
  null
);

INSERT INTO dish VALUES (
  1,
  'Chicken with Broccoli',
  'Diced chicken stir-fried with succulent broccoli florets',
  false
);

INSERT INTO dish VALUES (
  2,
  'Sweet and Sour Chicken',
  'Marinated chicken with tangy sweet and sour sauce together with pineapples and green peppers',
  false
);

INSERT INTO dish VALUES (
  3,
  'Chicken Wings',
  'Finger-licking mouth-watering entree to spice up any lunch or dinner',
  true
);

INSERT INTO dish VALUES (
  4,
  'Beef with Garlic Sauce',
  'Sliced beef steak marinated in garlic sauce for that tangy flavor',
  true
);

INSERT INTO dish VALUES (
  5,
  'Fresh Mushroom with Snow Peapods and Baby Corns',
  'Colorful entree perfect for vegetarians and mushroom lovers',
  false
);

INSERT INTO dish VALUES (
  6,
  'Sesame Chicken',
  'Crispy chunks of chicken flavored with savory sesame sauce',
  false
);

INSERT INTO dish VALUES (
  7,
  'Special Minced Chicken',
  'Marinated chicken breast sauteed with colorful vegetables topped with pine nuts and shredded lettuce.',
  false
);

INSERT INTO dish VALUES (
  8,
  'Hunan Special Half & Half',
  'Shredded beef in Peking sauce and shredded chicken in garlic sauce',
  true
);

INSERT INTO categories_dishes VALUES (
  'C',
  1,
  6.95
);

INSERT INTO categories_dishes VALUES (
  'C',
  3,
  6.95
);

INSERT INTO categories_dishes VALUES (
  'LS',
  1,
  8.95
);

INSERT INTO categories_dishes VALUES (
  'LS',
  4,
  8.95
);

INSERT INTO categories_dishes VALUES (
  'LS',
  5,
  8.95
);

INSERT INTO categories_dishes VALUES (
  'HS',
  6,
  15.95
);

INSERT INTO categories_dishes VALUES (
  'HS',
  7,
  16.95
);

INSERT INTO categories_dishes VALUES (
  'HS',
  8,
  17.95
);


SELECT restaurant.name, address.street_number, address.street_name, restaurant.phone_number
FROM restaurant, address;

SELECT MAX(rating) AS best_rating
FROM review;

-- SELECT dish.name, categories_dishes.price, category.name
-- FROM dish, categories_dishes, category
-- ORDER BY dish.name;

-- SELECT dish.name, categories_dishes.price, category.name
-- FROM dish INNER JOIN categories_dishes
--   ON dish.id = categories_dishes.dishes_id
--   INNER JOIN category 
--   ON categories_dishes.categories_id = category.id
-- ORDER BY dish.name;

SELECT dish.name, categories_dishes.price, category.name
FROM category, dish, categories_dishes
WHERE 
  categories_dishes.dishes_id = dish.id AND
  categories_dishes.categories_id = category.id
ORDER BY 1;

SELECT category.name, dish.name, categories_dishes.price
FROM category, dish, categories_dishes
WHERE 
  categories_dishes.dishes_id = dish.id AND
  categories_dishes.categories_id = category.id
ORDER BY 1;

SELECT dish.name AS spicy_dish_name, category.name, categories_dishes.price
FROM dish, category, categories_dishes
WHERE
  categories_dishes.dishes_id = dish.id AND
  categories_dishes.categories_id = category.id AND
  dish.hot_and_spicy = TRUE;

SELECT dishes_id, COUNT(dishes_id) AS dish_count
FROM categories_dishes
GROUP BY dishes_id
HAVING COUNT(dishes_id) > 1;

SELECT 
  dish.name AS dish_name, 
  COUNT(categories_dishes.dishes_id) AS dish_count
FROM dish, categories_dishes
WHERE dish.id = categories_dishes.dishes_id
GROUP BY dish_name
HAVING COUNT(categories_dishes.dishes_id) > 1;

SELECT MAX(rating) AS best_rating, description
FROM review
WHERE rating = (SELECT MAX(rating) FROM review)
GROUP BY description;