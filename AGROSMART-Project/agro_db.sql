
CREATE TABLE farmers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    location VARCHAR(100),
    phone VARCHAR(20),
    farm_size FLOAT,
    soil_ph FLOAT, 
    soil_type VARCHAR(50)
);
