import "./Hero.css";
import { Link } from "react-router-dom";
import { useEffect, useState } from "react";
import api from "../../api/api";

function Hero() {

  const [hero, setHero] = useState(null);

  const [loading, setLoading] = useState(true);

  useEffect(() => {

    api.get("hero/")
      .then((response) => {

        setHero(response.data);

      })
      .catch((error) => {

        console.error(error);

      })
      .finally(() => {

        setLoading(false);

      });

  }, []);

  if (loading) {

    return <section className="hero">Loading...</section>;

  }

  if (!hero) {

    return <section className="hero">No hero data found.</section>;

  }

  return (

    <section className="hero">

      <div className="hero-content">

        <span className="tag">

          {hero.tag}

        </span>

        <h1>

          {hero.title}

        </h1>

        <p>

          {hero.description}

        </p>

        <div className="hero-buttons">

          <Link
            to={hero.primary_button_link}
            className="primary-btn"
          >

            {hero.primary_button_text}

          </Link>

          <Link
            to={hero.secondary_button_link}
            className="secondary-btn"
          >

            {hero.secondary_button_text}

          </Link>

        </div>

      </div>

      <div className="hero-image">

        <img

          src={hero.image}

          alt={hero.title}

        />

      </div>

    </section>

  );

}

export default Hero;