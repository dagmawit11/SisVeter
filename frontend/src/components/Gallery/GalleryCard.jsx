import "./Gallery.css";

function GalleryCard(props) {

    console.log("GalleryCard props:", props);

    if (!props.item) {
        return <p>Item is undefined</p>;
    }

    const item = props.item;

    return (
        <div className="gallery-card">

            {item.media_type === "video" ? (
                <video controls>
                    <source src={item.file} type="video/mp4" />
                </video>
            ) : (
                <img src={item.file} alt={item.title} />
            )}

            <div className="gallery-content">
                <h3>{item.title}</h3>
                <p>{item.description}</p>
            </div>

        </div>
    );
}

export default GalleryCard;