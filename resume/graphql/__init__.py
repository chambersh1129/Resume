from urllib.parse import quote_plus

default_query = quote_plus(
    """{
  aboutMe {
    fullName
    title
    email
    github
    linkedin
  }
  workHistory(first: 2) {
    edges {
      node {
        company
        title
        startDate
        endDate
        totalTime
      }
    }
  }
  milestones(type: "edu") {
    edges {
      node {
        name
      }
    }
  }
}"""
)
