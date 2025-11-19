from supabase import create_client
from dotenv import load_dotenv
import os

load_dotenv()

SUPABASE_URL = os.getenv("https://yziiavkxztzssvhxhotb.supabase.co")
SUPABASE_KEY = os.getenv("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inl6aWlhdmt4enR6c3N2aHhob3RiIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc2MzU2MzkxOCwiZXhwIjoyMDc5MTM5OTE4fQ.SWkMxdY5V6R_ECiGHrkVK92SDQKere-WLX4XjzI-QpI")
")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
