import "./Contact.css";
import { useEffect, useState } from "react";
import api from "../../api/api";

import {
  FaPhoneAlt,
  FaEnvelope,
  FaMapMarkerAlt,
  FaClock,
  FaWhatsapp,
} from "react-icons/fa";

function Contact() {

  const [contact, setContact] = useState(null);

  useEffect(() => {
    api.get("contact/")
      .then((res) => setContact(res.data))
      .catch(console.error);
  }, []);

  if (!contact) return null;

  return (
    <section className="contact">

      <h2>Contact Us</h2>

      <p className="contact-description">
        We'd love to hear from you. Contact us today to book an appointment,
        ask a question, or learn more about our veterinary services.
      </p>

      <div className="contact-info-only">

        <div className="info-box">
          <FaPhoneAlt className="icon" />
          <div>
            <h3>Phone</h3>
            <p>{contact.phone}</p>
          </div>
        </div>

        <div className="info-box">
          <FaEnvelope className="icon" />
          <div>
            <h3>Email</h3>
            <p>{contact.email}</p>
          </div>
        </div>

        <div className="info-box">
          <FaMapMarkerAlt className="icon" />
          <div>
            <h3>Address</h3>
            <p>{contact.address}</p>
          </div>
        </div>

        <div className="info-box">
          <FaClock className="icon" />
          <div>
            <h3>Working Hours</h3>
            <p>{contact.working_days}</p>
            <p>{contact.working_hours}</p>
            <p>{contact.emergency_text}</p>
          </div>
        </div>

        <a
          href={`https://wa.me/${contact.whatsapp}`}
          target="_blank"
          rel="noreferrer"
          className="whatsapp-btn"
        >
          <FaWhatsapp />
          Chat on WhatsApp
        </a>

      </div>

    </section>
  );
}

export default Contact;