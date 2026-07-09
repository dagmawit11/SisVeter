import { useEffect, useState } from "react";
import ServiceCard from "./ServiceCard";
import api from "../../api/api";
import "./Services.css";

function Services() {

  const [services, setServices] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {

    api.get("services/")
      .then((response) => {
        setServices(response.data);
      })
      .catch((error) => {
        console.error("Error fetching services:", error);
      })
      .finally(() => {
        setLoading(false);
      });

  }, []);

  if (loading) {
    return (
      <section className="services">
        <h2>Our Services</h2>
        <p>Loading services...</p>
      </section>
    );
  }

  return (
    <section className="services">

      <h2>Our Services</h2>

      <div className="services-grid">

        {services.map((service) => (

          <ServiceCard
            key={service.id}
            icon={service.icon}
            title={service.title}
            description={service.description}
          />

        ))}

      </div>

    </section>
  );
}

export default Services;