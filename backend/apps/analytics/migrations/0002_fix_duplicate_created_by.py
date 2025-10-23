# Generated manually to fix duplicate created_by_id column issue

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('analytics', '0001_initial'),
    ]

    operations = [
        # This migration handles the case where created_by_id already exists
        # We'll use RunSQL to check if the column exists and handle it gracefully
        migrations.RunSQL(
            sql="""
            DO $$
            BEGIN
                -- Check if created_by_id column exists in analytics_reports table
                IF NOT EXISTS (
                    SELECT 1 
                    FROM information_schema.columns 
                    WHERE table_name = 'analytics_reports' 
                    AND column_name = 'created_by_id'
                ) THEN
                    -- Add the column if it doesn't exist
                    ALTER TABLE analytics_reports 
                    ADD COLUMN created_by_id integer;
                    
                    -- Add the foreign key constraint
                    ALTER TABLE analytics_reports 
                    ADD CONSTRAINT analytics_reports_created_by_id_fk 
                    FOREIGN KEY (created_by_id) REFERENCES auth_user(id) 
                    DEFERRABLE INITIALLY DEFERRED;
                    
                    -- Create index
                    CREATE INDEX analytics_reports_created_by_id_idx 
                    ON analytics_reports (created_by_id);
                END IF;
            END $$;
            """,
            reverse_sql="""
            -- Reverse operation - remove the column if it exists
            DO $$
            BEGIN
                IF EXISTS (
                    SELECT 1 
                    FROM information_schema.columns 
                    WHERE table_name = 'analytics_reports' 
                    AND column_name = 'created_by_id'
                ) THEN
                    ALTER TABLE analytics_reports DROP COLUMN created_by_id;
                END IF;
            END $$;
            """,
        ),
    ]
