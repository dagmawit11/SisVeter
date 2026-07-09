import { useEffect, useState } from "react";
import api from "../../api/api";
import "./Gallery.css";
import GalleryCard from "./GalleryCard";

function Gallery() {

  const [filter, setFilter] = useState("All");
  const [galleryItems, setGalleryItems] = useState([]);

  useEffect(() => {

    api.get("gallery/")
      .then((res) => {
        setGalleryItems(res.data);
      })
      .catch(console.error);

  }, []);

  const filteredItems =
    filter === "All"
      ? galleryItems
      : galleryItems.filter((item) => item.category === filter);

  return (

    <section className="gallery">

      <h2>Gallery</h2>

      <p className="gallery-description">
        Browse photos and videos of our wonderful patients,
        modern facilities, successful surgeries,
        and everyday veterinary care.
      </p>

      <div className="gallery-buttons">

        <button onClick={() => setFilter("All")}>All</button>
        <button onClick={() => setFilter("Pets")}>Pets</button>
        <button onClick={() => setFilter("Surgery")}>Surgery</button>
        <button onClick={() => setFilter("Videos")}>Videos</button>

      </div>

      <div className="gallery-grid">

        {filteredItems.map((item) => (

          <GalleryCard
            key={item.id}
            item={item}
          />

        ))}

      </div>

    </section>

  );
}

export default Gallery;