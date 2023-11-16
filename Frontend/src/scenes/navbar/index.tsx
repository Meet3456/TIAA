import { useState } from "react";
import { Bars3Icon, XMarkIcon } from "@heroicons/react/24/solid";
import Logo from "../../assets/logo_new.png";
import Link from "./Link";
import { SelectedPage } from "../../shared/types";
import useMediaQuery from "../../hooks/useMediaQuery";
import ActionButton from "../../shared/ActionButton";
import { useAuth0 } from "@auth0/auth0-react";
import { NavLink } from "react-router-dom";

type Props = {
    isTopOfPage: boolean;
    selectedPage: SelectedPage;
    setSelectPage: (value: SelectedPage) => void;
}

const Navbar = ({ isTopOfPage, selectedPage, setSelectPage }: Props) => {
    const flexBetween = "flex items-center justify-between";
    const isAboveMediumScreens = useMediaQuery("(min-width: 1060px)");
    const [isMenuToggled, setIsMenuToggled] = useState<boolean>(false);
    const navbarBackground = isTopOfPage ? "" : "bg-primary-100 drop-shadow";
    const { loginWithRedirect, isAuthenticated, logout } = useAuth0();

    return (
        <nav>
            <div
                className={`${navbarBackground} ${flexBetween} bg-primary-100 fixed top-0 z-30 w-full py-6`}
            >
                <div className={`${flexBetween} mx-auto w-5/6`}>
                    <div className={`${flexBetween} w-full gap-16`}>
                        {/* LEFT SIDE */}
                        <img alt="logo" src={Logo} className="w-44 h-7" />

                        {isAboveMediumScreens ? (
                            <div className={`${flexBetween} w-full`}>
                                <div className={`${flexBetween} gap-8 text-sm`}>
                                    <Link page="Home"
                                        selectedPage={selectedPage}
                                        setSelectPage={setSelectPage}
                                    />
                                    <Link page="Benefits"
                                        selectedPage={selectedPage}
                                        setSelectPage={setSelectPage}
                                    />
                                    <Link page="About Us"
                                        selectedPage={selectedPage}
                                        setSelectPage={setSelectPage}
                                    />
                                    <Link page="Contact Us"
                                        selectedPage={selectedPage}
                                        setSelectPage={setSelectPage} />

                                </div>
                                <div className={`${flexBetween} gap-8`}>
                                    {isAuthenticated ? (
                                        // User is authenticated, show "Get Started" button
                                        // <ActionButton label="Get Started" onClick={logout} />
                                        <NavLink to='/home'>
                                            <button className={`${flexBetween} gap-8 rounded bg-secondary-500 p-2 hover:bg-primary-500 hover:text-white w-[150px] pl-5`} >
                                                Get Started
                                            </button>
                                        </NavLink>
                                    ) : (
                                        // User is not authenticated, show "Sign In" button
                                        <div className={`${flexBetween} gap-8`} onClick={() => loginWithRedirect()}>
                                            Sign in
                                        </div>
                                    )}
                                </div>
                            </div>) : (
                            <button
                                className="rounded-full bg-secondary-500 p-2 "
                                onClick={() => setIsMenuToggled(!isMenuToggled)}>
                                <Bars3Icon className="h-6 w-6 text-white" />
                            </button>
                        )}
                    </div>
                </div>
            </div>

            {/* Mobile Menu */}
            {!isAboveMediumScreens && isMenuToggled && (
                <div className="fixed right-0 bottom-0 z-40 h-full w-[300px] bg-primary-100 drop-shadow-xl">
                    {/* CLOSE ICON */}
                    <div className="flex justify-end p-12">
                        <button onClick={() => setIsMenuToggled(!isMenuToggled)}>
                            <XMarkIcon className="h-6 w-6 text-gray-400" />
                        </button>
                    </div>

                    {/* MENU ITEMS */}
                    <div className="ml-[33%] flex flex-col gap-10 text-2xl">
                        <Link
                            page="Home"
                            selectedPage={selectedPage}
                            setSelectPage={setSelectPage}
                        />
                        <Link
                            page="Benefits"
                            selectedPage={selectedPage}
                            setSelectPage={setSelectPage}
                        />
                        <Link
                            page="About Us"
                            selectedPage={selectedPage}
                            setSelectPage={setSelectPage}
                        />
                        <Link
                            page="Contact Us"
                            selectedPage={selectedPage}
                            setSelectPage={setSelectPage}
                        />
                    </div>
                </div>
            )}
        </nav>
    )
}

export default Navbar;
