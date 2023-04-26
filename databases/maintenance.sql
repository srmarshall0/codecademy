SELECT pg_size_pretty(
  pg_table_size('sensors.observations')
) as table_size;

SELECT pg_size_pretty(
  pg_indexes_size('sensors.observations')
) as index_size;

SELECT pg_size_pretty(
  pg_total_relation_size('sensors.observations')
) as relation_size;

UPDATE sensors.observations
SET distance = distance*3.281
WHERE TRUE;

select pg_size_pretty(
  pg_total_relation_size('sensors.observations')
) as relation_post_update;

VACUUM sensors.observations;

select pg_size_pretty(
  pg_total_relation_size('sensors.observations')
) as relation_post_vacuum;

\COPY sensors.observations (id, datetime, location_id, duration, distance, category) FROM './additional_obs_types.csv' WITH DELIMITER ',' CSV HEADER;

select pg_size_pretty(
  pg_table_size('sensors.observations')
) as table_post_insert;

VACUUM FULL sensors.observations;

select pg_size_pretty(
  pg_table_size('sensors.observations')
) as table_post_full_vacuum;

delete from sensors.observations
where location_id > 24;

select pg_size_pretty(
  pg_table_size('sensors.observations')
) as table_post_delete;

truncate sensors.observations;

\COPY sensors.observations (id, datetime, location_id, duration, distance, category) FROM './additional_obs_types.csv' WITH DELIMITER ',' CSV HEADER;

select pg_size_pretty(
  pg_table_size('sensors.observations')
) as table_post_mass_insert;









