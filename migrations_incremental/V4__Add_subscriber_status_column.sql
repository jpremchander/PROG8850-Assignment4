-- Incremental migration: Add 'status' column to 'subscribers' table
ALTER TABLE subscribers ADD COLUMN status VARCHAR(20) DEFAULT 'active';
