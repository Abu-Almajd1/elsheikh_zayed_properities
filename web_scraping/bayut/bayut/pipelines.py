import psycopg2

class PostgresPipeline:
    def open_spider(self, spider):
        """Connect to PostgreSQL when the spider starts."""
        self.conn = psycopg2.connect(
            host=spider.settings.get("POSTGRES_HOST"),
            database=spider.settings.get("POSTGRES_DB"),
            user=spider.settings.get("POSTGRES_USER"),
            password=spider.settings.get("POSTGRES_PASSWORD"),
            port=spider.settings.get("POSTGRES_PORT")
        )
        self.cur = self.conn.cursor()

    def process_item(self, item, spider):
        """Insert data into PostgreSQL."""
        self.cur.execute(
            """
            INSERT INTO bayut_data (
                url, title, price_amount, location_address, bedrooms, bathrooms, property_area,
                description, type, purpose, reference, completion_status, furnishing_status,
                date_posted, ownership, amenities, agent_name
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """,
            (
                item.get("url", ""),
                item.get("title", ""),
                item.get("price_amount", ""),
                item.get("location_address", ""),
                item.get("bedrooms", ""),
                item.get("bathrooms", ""),
                item.get("property_area", ""),
                item.get("description", ""),
                item.get("type", ""),
                item.get("purpose", ""),
                item.get("reference", ""),
                item.get("completion_status", ""),
                item.get("furnishing_status", ""),
                item.get("date_posted", ""),
                item.get("ownership", ""),
                ",".join(item.get("amenities", [])), 
                item.get("agent_name", "")
            )
        )
        self.conn.commit()
        return item

    def close_spider(self, spider):
        """Close the database connection when the spider finishes."""
        self.cur.close()
        self.conn.close()
