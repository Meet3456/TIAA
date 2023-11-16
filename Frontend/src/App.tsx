import Navbar from "../src/scenes/navbar"
import { useEffect, useState } from "react";
import { SelectedPage } from "./shared/types";
import Home from "./scenes/home";
import About from "./scenes/about";
import Contact from "./scenes/contact";
import Benefits from "./scenes/benefits";
import Footer from "./scenes/Footer";

export default function App() {
  const [selectedPage, setSelectedPage] = useState<SelectedPage>(
    SelectedPage.Home
  );
  const [isTopOfPage, setIsTopOfPage] = useState<boolean>(true);

  useEffect(() => {
    const handleScroll = () => {
      const scrollTop = window.scrollY;
      setIsTopOfPage(scrollTop === 0);
      console.log("scrolled")
    };

    // Attach the event listener
    window.addEventListener('scroll', handleScroll);

    // Detach the event listener when the component is unmounted
    return () => {
      window.removeEventListener('scroll', handleScroll);
    };
  }, []); 

  return (
    <div className="app bg-gray-20">
      <Navbar
        isTopOfPage={isTopOfPage}
        selectedPage={selectedPage}
        setSelectPage={setSelectedPage}
      />
      <Home setSelectPage={setSelectedPage}/>
      <Benefits setSelectedPage={setSelectedPage}/>
      <About setSelectedPage={setSelectedPage}/>
      <Contact setSelectedPage={setSelectedPage}/>
      <Footer/>
    </div>
  );
}