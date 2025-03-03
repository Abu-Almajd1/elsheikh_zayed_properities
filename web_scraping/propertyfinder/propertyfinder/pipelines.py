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
            INSERT INTO propertyfinder_data (
                url, title, price, location, property_type, bedrooms, bathrooms, 
                area, available_from, description, amenities
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """,
            (
                item.get("url", ""),
                item.get("title", ""),
                item.get("price", ""),
                item.get("location", ""),
                item.get("property_type", ""),
                item.get("bedrooms", ""),
                item.get("bathrooms", ""),
                item.get("area", ""),
                item.get("available_from", ""),
                item.get("description", ""),
                ",".join(item.get("amenities", []))  
            )
        )
        self.conn.commit()
        return item

    def close_spider(self, spider):
        """Close the database connection when the spider finishes."""
        self.cur.close()
        self.conn.close()
