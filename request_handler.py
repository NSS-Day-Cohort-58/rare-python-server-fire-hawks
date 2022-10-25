from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from views.category_requests import get_all_categorys, get_single_category, create_category, delete_category
from views.comments_requests import create_comment, get_all_comments, get_single_comment, delete_comment
from views.post_reactions_requests import get_all_post_reactions, get_single_post_reaction, create_post_reaction, delete_post_reaction
from views.post_requests import create_post, delete_post, get_all_posts, get_single_post
from views.post_requests import delete_post, get_all_posts, get_single_post
from views.post_tags_requests import create_post_tag, get_all_post_tags, get_single_post_tag, delete_post_tag
from views.reaction_requests import create_reaction, get_all_reactions, get_single_reaction, delete_reaction
from views.subscribe_requests import create_subscription, get_all_subscriptions, get_single_subscription, delete_subscription
from views.tag_requests import create_tag, get_all_tags, get_single_tag, delete_tag
from views.user_requests import create_user, delete_user, get_all_users, get_single_user, login_user

method_mapper = {
    "posts": {
        "single": get_single_post,
        "all": get_all_posts
    },
    "categories": {
        "single": get_single_category,
        "all": get_all_categorys
    },
    "tags": {
        "single": get_single_tag,
        "all": get_all_tags
    },
    "users": {
        "single": get_single_user,
        "all": get_all_users
    },
    "reactions": {
        "single": get_single_reaction,
        "all": get_all_reactions
    },
    "postReactions": {
        "single": get_single_post_reaction,
        "all": get_all_post_reactions
    },
    "postTags": {
        "single": get_single_post_tag,
        "all": get_all_post_tags
    },
    "subscriptions": {
        "single": get_single_subscription,
        "all": get_all_subscriptions
    }
}


class HandleRequests(BaseHTTPRequestHandler):
    """Handles the requests to this server"""

    def parse_url(self, path):
        """Parse the url into the resource and id"""
        path_params = self.path.split('/')
        resource = path_params[1]
        if '?' in resource:
            param = resource.split('?')[1]
            resource = resource.split('?')[0]
            pair = param.split('=')
            key = pair[0]
            value = pair[1]
            return (resource, key, value)
        else:
            id = None
            try:
                id = int(path_params[2])
            except (IndexError, ValueError):
                pass
            return (resource, id)

    def _set_headers(self, status):
        """Sets the status code, Content-Type and Access-Control-Allow-Origin
        headers on the response

        Args:
            status (number): the status code to return to the front end
        """
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    def do_OPTIONS(self):
        """Sets the OPTIONS headers
        """
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods',
                         'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers',
                         'X-Requested-With, Content-Type, Accept')
        self.end_headers()

    def get_all_or_single(self, resource, id):
        if id is not None:
            response = method_mapper[resource]["single"](id)

            if response is not None:
                self._set_headers(200)
            else:
                self._set_headers(404)
                response = ''
        else:
            self._set_headers(200)
            response = method_mapper[resource]["all"]()

        return response

    def do_GET(self):
        self._set_headers(200)
        response = {}
        parsed = self.parse_url(self.path)

    # Parse URL and store entire tuple in a variable

        # If the path does not include a query parameter, continue with the original if block
        if '?' not in self.path:
            (resource, id) = parsed

            if resource == "posts":
                if id is not None:
                    response = get_single_post(id)
                else:
                    response = get_all_posts()

            if resource == "categories":
                if id is not None:
                    response = get_single_category(id)
                else:
                    response = get_all_categorys()
            if resource == "users":
                if id is not None:
                    response = get_single_user(id)
                else:
                    response = get_all_users()
            if resource == "comments":
                if id is not None:
                    response = get_single_comment(id)
                else:
                    response = get_all_comments()
                    
            if resource == "reactions":
                if id is not None:
                    response = get_single_reaction(id)
                else:
                    response = get_all_reactions()
            if resource == "tags":
                if id is not None:
                    response = get_single_tag(id)
                else:
                    response = get_all_tags()
            if resource == "postReactions":
                if id is not None:
                    response = get_single_post_reaction(id)
                else:
                    response = get_all_post_reactions()
            if resource == "postTags":
                if id is not None:
                    response = get_single_post_tag(id)
                else:
                    response = get_all_post_tags()
            if resource == "subscriptions":
                if id is not None:
                    response = get_single_subscription(id)
                else:
                    response = get_all_subscriptions()

            

        self.wfile.write(response.encode())

    def do_POST(self):
        """Make a post request to the server"""
        self._set_headers(201)
        content_len = int(self.headers.get('content-length', 0))
        post_body = json.loads(self.rfile.read(content_len))
        response = ''
        resource, _ = self.parse_url(self.path)

        if resource == 'login':
            response = login_user(post_body)
        if resource == 'register':
            response = create_user(post_body)
        if resource == 'categories':
            response = create_category(post_body)
        if resource == 'comments':
            response = create_comment(post_body)
        if resource == 'tag':
            response = create_tag(post_body)
        if resource == 'users':
            response = create_user(post_body)
        if resource == 'reactions':
            response = create_reaction(post_body)
        if resource == 'posts':
            response = create_post(post_body)
        if resource == 'postReactions':
            response = create_post_reaction(post_body)
        if resource == 'postTags':
            response = create_post_tag(post_body)
        if resource == 'subscriptions':
            response = create_subscription(post_body)

        self.wfile.write(response.encode())

    def do_PUT(self):
        """Handles PUT requests to the server"""
        pass

    def do_DELETE(self):
        self._set_headers(204)

        (resource, id) = self.parse_url(self.path)

        if resource == "posts":
            delete_post(id)
        if resource == "comments":
            delete_comment(id)
        if resource == "subscriptions":
            delete_subscription(id)
        if resource == "tags":
            delete_tag(id)
        if resource == "categories":
            delete_category(id)
        if resource == "postReactions":
            delete_post_reaction(id)
        if resource == "postTags":
            delete_post_tag(id)
        if resource == "reactions":
            delete_reaction(id)
        if resource == "users":
            delete_user(id)

        self.wfile.write("".encode())


def main():
    """Starts the server on port 8088 using the HandleRequests class
    """
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()
