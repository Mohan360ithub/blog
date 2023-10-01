import frappe

def get_context(abc):
    blogs = frappe.get_list(
                            "Userblog",
                            filters={"published":1},
                            fields=["title","sub_title","banner_image","creator","published","route"],                        
                            )
    abc.blogs = blogs
    
    abc.blr = ["btm","jpnagar","jayanagar","koramangala"]

    


# title,
# sub_title,
# banner_image,
# column_break_jqti,
# creator,
# published,
# route,
# section_break_mzfu,
# body