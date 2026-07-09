import {
  FaDog,
  FaSyringe,
  FaStethoscope,
  FaTooth,
  FaCut,
  FaAmbulance,
} from "react-icons/fa";

const iconMap = {
  dog: FaDog,
  syringe: FaSyringe,
  stethoscope: FaStethoscope,
  tooth: FaTooth,
  cut: FaCut,
  ambulance: FaAmbulance,
};

function ServiceCard({ icon, title, description }) {
  const Icon = iconMap[icon] || FaDog;

  return (
    <div className="service-card">
      <div className="service-icon">
        <Icon />
      </div>

      <h3>{title}</h3>
      <p>{description}</p>
    </div>
  );
}

export default ServiceCard;