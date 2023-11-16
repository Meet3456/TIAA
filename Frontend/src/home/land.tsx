import CustomCard from "."; // Make sure to provide the correct path
import { useAuth0 } from "@auth0/auth0-react";
import logo from '../assets/logo_new.png'
import { NavLink } from "react-router-dom";
import planning from '../assets/planning.jpg'
import advisor from '../assets/advisor.jpeg'
import healthcare from '../assets/healthcare.jpg'
import community from '../assets/community.jpg'
import finance from '../assets/finance.jpg'
import explorer from '../assets/explorer.jpg'
import Footer from "../scenes/Footer";
const Land = () => {
    const { user, isAuthenticated, isLoading } = useAuth0();
    const flexBetween = "flex items-center justify-between";

    if (isLoading) {
        return <div>Loading ...</div>;
    }
    return (

        <div className="bg-primary-100 ">
            {/* <button onClick={() => logout({ logoutParams: { returnTo: window.location.origin } })}>
                Log Out
            </button> */}
            <nav className="bg-white border-gray-200 dark:bg-primary-300">
                <div className="flex flex-wrap justify-between items-center mx-auto max-w-screen-xl p-4">
                    <a href="https://flowbite.com" className="flex items-center space-x-3 rtl:space-x-reverse">
                        <img src={logo} className="h-6 " alt="Flowbite Logo" />
                    </a>
                    <div className="flex space-x-4 items-center">
                        {isAuthenticated && (
                            <div>
                                <h2 className="text-white">Hello, {user.name} :) </h2>
                            </div>
                        )}
                        <NavLink to='/'>
                            <button className={`${flexBetween} gap-8 rounded bg-secondary-500 p-2 hover:bg-primary-500 hover:text-white w-[120px] pl-5`}>
                                Log Out
                            </button>
                        </NavLink>
                    </div>
                </div>
            </nav>
            <div className="flex items-center mt-[5%] h-screen flex flex-col">
                <strong><h1 className="text-2xl new ">Embark on a Journey: Your Retirement with Us!</h1></strong>
                <br />
                <div className="grid grid-cols-1 sm:grid-cols-1 md:grid-cols-2 lg:grid-cols-2 gap-3 m-2 bg-primary-100">
                    <NavLink to='/planning'><CustomCard heading="Retirement Planning 🚀" text="Plan your retirement." image={planning} /></NavLink>
                    <NavLink to='/community'><CustomCard heading="Social Engagement Community 🌐" text="Build a community together" image={community} /></NavLink>
                    <NavLink to="http://localhost:8501"><CustomCard heading="Robo Advisor 🤖" text="Get Ai Advice" image={advisor} /></NavLink>
                    <NavLink to="http://localhost:8502"><CustomCard heading="HealthCare 🩺" text="know Insurance cost." image={healthcare} /></NavLink>
                    <NavLink to="http://localhost:8503"><CustomCard heading="Finance Bot ✅" text="Stock bot" image={finance} /></NavLink>
                    <NavLink to="http://localhost:8504"><CustomCard heading="NearMe Explorer 📍" text="Map explorer" image={explorer} /></NavLink>
                </div>
            </div>
            <Footer/>

        </div>
        
    );
}

export default Land;
