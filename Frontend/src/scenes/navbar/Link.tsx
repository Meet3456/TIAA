import AnchorLink from "react-anchor-link-smooth-scroll"
import { SelectedPage } from "../../shared/types";

type Props = {
    page : string
    selectedPage: SelectedPage;
    setSelectPage : (value : SelectedPage) => void;
}

const Link = ({page, selectedPage, setSelectPage
}:Props) => {
    const lowerCasePage = page.toLowerCase().replace(/ /g, "") as SelectedPage; 
 return (
    <AnchorLink
    className={`${selectedPage === lowerCasePage ? "text-primary-500" : ""}
    transition duration-500 hover:text-primary-300
    `}
    href={`#${lowerCasePage}`}
    onClick={()=> setSelectPage(lowerCasePage)}
    >
        {page}
    </AnchorLink>
 )


}    

export default Link