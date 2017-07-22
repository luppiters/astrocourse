#Large stars:
Select radius, t_eff from Star where radius > 1;

#A range of hot stars:
Select kepler_id, t_eff from Star
where t_eff between 5000 and 6000;


#Confirmed exoplanets:
Select kepler_name, radius from Planet
WHERE (kepler_name is not NULL) and (radius between 1 and 3);

#Planet statistics:
select min(radius), max(radius), avg(radius), stddev(radius)
from Planet where kepler_name is NULL;

#Select kepler_id, COUNT(koi_name) from Planet
group by kepler_id having COUNT(koi_name) > 1 order by 2 desc;

#Systems with small planets:
select s.radius as sun_radius, p.radius as planet_radius
from Star as s, Planet as p
where (s.radius > p.radius) and (s.kepler_id = p.kepler_id)
order by 1 desc;

#How many planets for big stars?
select s.radius, count(p.koi_name) from Star as s
join Planet as p on s.kepler_id = p.kepler_id and s.radius > 1
group by s.kepler_id 
having count(p.kepler_id) > 1 order by 1 desc;

#Lonely stars:
select s.kepler_id, s.t_eff, s.radius from Star as s
LEFT OUTER JOIN Planet as p using (kepler_id)
where p.koi_name is null
order by s.t_eff desc;

#Subquery joint stars and planets:
SELECT ROUND(AVG(p.t_eq), 1), MIN(s.t_eff), MAX(s.t_eff)
FROM Star s
JOIN Planet p USING(kepler_id)
WHERE S.t_eff > (
  SELECT AVG(t_eff) FROM Star
);

#Correlated sizes?
select p.koi_name, p.radius, s.radius from Planet p
join Star s using (kepler_id)
WHERE s.kepler_id in (
  SELECT kepler_id FROM Star
  ORDER BY radius DESC
  LIMIT 5
);

