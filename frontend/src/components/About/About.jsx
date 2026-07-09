import "./About.css";
import { FaCheckCircle } from "react-icons/fa";
import { useEffect, useState } from "react";
import api from "../../api/api";

function About() {

  const [about, setAbout] = useState(null);

  useEffect(() => {

    api.get("about/")

      .then((res) => {

        setAbout(res.data);

      })

      .catch(console.error);

  }, []);

  if (!about) {

    return null;

  }

  return (

    <section className="about">

      <div className="about-image">

        <img
          src={about.image}
          alt={about.title}
        />

      </div>

      <div className="about-content">

        <span className="section-title">

          {about.welcome_text}

        </span>

        <h2>

          {about.title}

        </h2>

        <p>

          {about.description}

        </p>

        <div className="features">

          <div className="feature">

            <FaCheckCircle />

            <span>{about.feature1}</span>

          </div>

          <div className="feature">

            <FaCheckCircle />

            <span>{about.feature2}</span>

          </div>

          <div className="feature">

            <FaCheckCircle />

            <span>{about.feature3}</span>

          </div>

          <div className="feature">

            <FaCheckCircle />

            <span>{about.feature4}</span>

          </div>

        </div>

      </div>

    </section>

  );

}

export default About;