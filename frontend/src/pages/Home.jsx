import Hero from "../components/Hero/Hero";
import About from "../components/About/About";
import Services from "../components/Services/Services";
import Gallery from "../components/Gallery/Gallery";
import Contact from "../components/Contact/Contact";




function Home() {
  return (
    <>
      <Hero />
      <About/>
      <Services/>
      <Gallery/>
      <Contact/>
    </>
  );
}

export default Home;